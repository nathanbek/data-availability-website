import argparse
import os

import fiona
import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.patches import Patch
from shapely.geometry import LineString, MultiPoint, Point, Polygon, box


def calculate_distance(geometry):
    if isinstance(geometry, MultiPoint):
        points = [point for point in geometry.geoms]
        line = LineString(points)
        return round(line.length / 1000, 2)  # Convert meters to kilometers and round to the nearest hundredth
    elif isinstance(geometry, LineString):
        return round(geometry.length / 1000, 2)  # Convert meters to kilometers and round to the nearest hundredth
    elif isinstance(geometry, Point):
        return 0  # A single point has no length
    else:
        return 0  # Handle other geometry types accordingly

def determine_availability(row):
    if row['availability'] == 's':
        return 'yes'
    elif row['availability'] == 'u':
        return 'no'
    else:
        return 'outdated'

def plot_data_on_basemap(basemap, gdf, institution, filename, output_folder):
    # Define the colors for the categories
    category_colors = {
        'Ocean': '#a3bdd1',
        'Ice shelf': '#cfe1eb',
        'Land': '#f0f0f0',
        'Sub-antarctic_G': 'lightgreen',
        'Sub-antarctic_L': 'lightblue',
        'Ice tongue': 'lightgrey',
        'Rumple': '#f0f0f0',
    }

    fig, ax = plt.subplots(figsize=(15, 15), dpi=600)  # Larger size and higher DPI for better quality

    # Set background color to white
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')

    # Plot basemap with custom colors
    basemap['color'] = basemap['Category'].map(category_colors)

    # Split basemap into inside and outside the circle
    center = Point(0, 0)
    radius = 3.3e6  # Increase radius slightly for zoom out

    circle_poly = center.buffer(radius)

    inside_circle = basemap[basemap.geometry.intersects(circle_poly)]
    outside_circle = basemap[~basemap.geometry.intersects(circle_poly)]

    # Plot the 'Ocean' category differently inside and outside the circle
    for category, color in category_colors.items():
        inside = inside_circle[inside_circle['Category'] == category]
        outside = outside_circle[outside_circle['Category'] == category]

        # Inside circle: plot with original color
        if not inside.empty:
            inside.plot(ax=ax, color=color, edgecolor='none')  # Remove edge color for better visibility

        # Outside circle: plot with white color for 'Ocean'
        if not outside.empty:
            outside.plot(ax=ax, color='white' if category == 'Ocean' else color, edgecolor='black')

    # Define colors and labels based on availability
    availability_colors = {'u': '#fb9a99', 's': '#1f78bc', 'a': '#888888'}
    availability_labels = {'u': 'Unavailable', 's': 'Available', 'a': 'Outdated'}

    # Plot the data for the institution
    if not gdf.empty:
        # Plot 'u' (unavailable) first
        for availability in ['u', 'a']:
            subset = gdf[gdf['availability'] == availability]
            if not subset.empty:
                color = availability_colors.get(availability, 'darkgrey')
                label = availability_labels.get(availability, 'Other')
                subset.plot(ax=ax, color=color, markersize=0.00055 if 'MultiPoint' in subset.geometry.type.unique() else 0.55, linewidth=0.55, label=label)

        # Plot 's' (available) last to ensure it's on top
        subset = gdf[gdf['availability'] == 's']
        if not subset.empty:
            subset.plot(ax=ax, color=availability_colors['s'], markersize=0.00055 if 'MultiPoint' in subset.geometry.type.unique() else 0.55, linewidth=0.55, label=availability_labels['s'])

    # Debug: print GeoDataFrame information
    print("Institution GeoDataFrame:")
    print(gdf.head())

    # Set limits to zoom out slightly on Antarctica
    ax.set_xlim(-3.3e6, 3.3e6)  # Increase to zoom out slightly
    ax.set_ylim(-3.3e6, 3.3e6)  # Increase to zoom out slightly

    # Set equal aspect ratio for circular plot and remove axes
    ax.set_aspect('equal')
    ax.axis('off')

    # Add a custom scale bar
    scalebar_length_km = 1000  # Length of scale bar in kilometers
    scalebar_length_m = scalebar_length_km * 1000  # Convert to meters

    # Calculate the position and draw the scale bar
    scalebar_x = -2.7e6  # Adjusted to fit within new zoom level
    scalebar_y = -3.0e6  # Adjusted to fit within new zoom level
    ax.plot([scalebar_x, scalebar_x + scalebar_length_m], [scalebar_y, scalebar_y], color='black', lw=2)
    ax.text(scalebar_x + scalebar_length_m / 2, scalebar_y - 2e5, f'{scalebar_length_km} km', ha='center', va='top')

    plt.title(f'{institution} Data Availability', fontsize=14)

    # Handle legend
    legend_patches = [Patch(color=color, label=availability_labels[availability]) for availability, color in availability_colors.items()]
    ax.legend(handles=legend_patches, loc='upper right', fontsize=8, title='Availability')

    # Draw a circular boundary
    bbox_size = 4.2e6  # Adjusted to match the new zoom level
    bbox = box(-bbox_size, -bbox_size, bbox_size, bbox_size)

    # Create the mask polygon with the bounding box as the outer boundary and the circle as a hole
    mask = Polygon(bbox.exterior.coords, [circle_poly.exterior.coords])

    # Convert the mask to a matplotlib patch
    mask_patch = plt.Polygon(list(mask.exterior.coords) + list(mask.interiors[0].coords), closed=True, facecolor='white', edgecolor='none')
    ax.add_patch(mask_patch)

    # Draw the circle outline in white
    circle = plt.Circle((0, 0), radius, facecolor='none', edgecolor='white', linewidth=1)
    ax.add_artist(circle)

    # Save the plot to the data folder with higher DPI and in PNG format
    output_path = os.path.join(output_folder, filename)
    plt.savefig(output_path, bbox_inches='tight', pad_inches=0.1, dpi=300)
    plt.close(fig)
    print(f"Saved map for {institution} to {output_path}")

def main(input_file_path, map_path, output_folder="maps"):
    # Ensure the output folders exist
    os.makedirs(output_folder, exist_ok=True)

    # Read the GeoPackage file into a GeoDataFrame
    fp = gpd.read_file(input_file_path)

    # Read the map shapefile
    mp = gpd.read_file(map_path)

    # Check if the 'Category' column exists
    if 'Category' not in mp.columns:
        print("The 'Category' column does not exist in the GeoDataFrame.")
        return

    # Define the colors for the categories
    category_colors = {
        'Ocean': '#a3bdd1',
        'Ice shelf': '#cfe1eb',
        'Land': '#f0f0f0',
        'Sub-antarctic_G': 'lightgreen',
        'Sub-antarctic_L': 'lightblue',
        'Ice tongue': 'lightgrey',
        'Rumple': 'yellow',
    }

    # Create a color column based on the 'Category' column
    mp['color'] = mp['Category'].map(category_colors).fillna('grey')  # Default to grey for undefined categories

    try:
        layers = fiona.listlayers(input_file_path)
        if not layers:
            raise ValueError("No layers found in the GeoPackage.")
        print("Layers in the GeoPackage:")
        print(layers)
    except Exception as e:
        print(f"Error listing layers in the GeoPackage: {e}")
        return

    # Create a dictionary to map institutions to layers
    institution_layers = {}

    # Populate the dictionary
    for layer in layers:
        try:
            gdf = gpd.read_file(input_file_path, layer=layer)  # Read the full layer
            if 'institution' in gdf.columns:
                institutions = gdf['institution'].unique()
                for institution in institutions:
                    if institution not in institution_layers:
                        institution_layers[institution] = []
                    institution_layers[institution].append(layer)
        except Exception as e:
            print(f"Error reading layer {layer}: {e}")

    print("Institution layers mapping:")
    print(institution_layers)

    # Create an overview GeoDataFrame
    overview_gdf = gpd.GeoDataFrame()

    # Iterate through each institution and create maps
    for institution, layers in institution_layers.items():
        institution_data = []

        print(f"\nProcessing institution: {institution}")

        for layer in layers:
            print(f"Checking layer: {layer}")
            try:
                gdf = gpd.read_file(input_file_path, layer=layer)  # Read the full layer

                if 'institution' in gdf.columns and institution in gdf['institution'].unique():
                    print(f"Layer '{layer}' contains '{institution}'.")
                    institution_data.append(gdf[gdf['institution'] == institution])
                else:
                    print(f"Layer '{layer}' does not contain '{institution}' or does not have 'institution' column.")
            except Exception as e:
                print(f"Error processing layer {layer}: {e}")

        # Combine all dataframes for the institution
        if institution_data:
            institution_gdf = gpd.GeoDataFrame(pd.concat(institution_data, ignore_index=True))
        else:
            institution_gdf = gpd.GeoDataFrame()

        # Ensure the CRS matches between the basemap and the GeoDataFrame
        if not institution_gdf.empty:
            institution_gdf = institution_gdf.to_crs(mp.crs)

        # Add to the overview GeoDataFrame
        if not institution_gdf.empty:
            overview_gdf = pd.concat([overview_gdf, institution_gdf])

        # Plot and save the aggregated data for the institution
        plot_data_on_basemap(mp, institution_gdf, institution, f'Antarctica_coverage_{institution}.png', output_folder)

    # Ensure the CRS matches between the basemap and the overview GeoDataFrame
    if not overview_gdf.empty:
        overview_gdf = gpd.GeoDataFrame(overview_gdf).to_crs(mp.crs)

    # Plot and save the overview map
    plot_data_on_basemap(mp, overview_gdf, "Overview", 'Antarctica_coverage_overview.png', output_folder)

    print("All maps have been created and saved to the data3 folder.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate maps from GeoPackage data.')
    parser.add_argument('input_file_path', type=str, help='Path to the GeoPackage input file.')
    parser.add_argument('map_path', type=str, help='Path to the map shapefile.')
    parser.add_argument('output_folder', type=str, help='Folder to save the generated maps.')

    args = parser.parse_args()
    main(args.input_file_path, args.map_path, args.output_folder)



# python3 scripts/generate_maps.py /Users/nathanbekele/Documents/CodingProjects/Research/antarctic_index.gpkg /Users/nathanbekele/Downloads/Quantarctica3/Miscellaneous/SimpleBasemap/ADD_DerivedLowresBasemap.shp scripts/data1
