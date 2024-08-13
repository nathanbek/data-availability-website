# QIceRadar Website

## Overview

The QIceRadar website is designed to visualize and provide access to data collected by various institutions on Antarctic research. This website is built with HTML, CSS, JavaScript, and Bootstrap and is deployed using GitHub Pages for continuous deployment and easy updates.

## Table of Contents

1. [Getting Started](#getting-started)
2. [Installation](#installation)
3. [Development](#development)
4. [Deployment](#deployment)
5. [Project Structure](#project-structure)
6. [Updating the Website](#updating-the-website)
7. [Automated Updates](#automated-updates)
8. [Troubleshooting](#troubleshooting)
9. [Acknowledgements](#acknowledgements)
10. [Future Updates](#future-updates)
11. [Contact](#contact)

## Getting Started

To get started with the QIceRadar website, you'll need to have some tools installed on your local machine:

- [Node.js](https://nodejs.org/) (LTS version recommended)
- [npm](https://www.npmjs.com/)

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/your-username/qiceradar-website.git
   cd qiceradar-website
   ```

2. **Install dependencies:**

   ```sh
   npm install
   ```

## Development

To start a local development server and begin working on the website, you can use a simple HTTP server. Here's how to do it with `http-server`:

1. **Install http-server globally:**

   ```sh
   npm install -g http-server
   ```

2. **Start the server:**

   ```sh
   http-server -c-1
   ```

   This command will start the HTTP server, and you can view the website at `http://localhost:8080`.

## Deployment

The website is deployed on GitHub Pages using an automated process through GitHub Actions. To deploy updates, follow these steps:

1. **Commit your changes:**

   Ensure your site is ready for deployment by committing any changes to the main branch. The GitHub Actions workflow will handle the deployment to the `gh-pages` branch.

2. **GitHub Actions Workflow:**

   The site is automatically updated daily with new data using a custom GitHub Actions workflow. This workflow pulls the latest data, regenerates the maps, and pushes the changes to the `gh-pages` branch, which triggers a deployment.

## Project Structure

Here's a brief overview of the project's structure:

```bash
qiceradar-website/
├── index.html                 # Home page
├── maps.html                  # Maps page
├── csvs.html                  # CSV Data page
├── about.html                 # About page
├── css/
│   └── styles.css             # Custom styles
├── js/
│   └── scripts.js             # Custom scripts
├── assets/
│   ├── images/                # Image assets
│   ├── csvs/                  # CSV data files
│   └── maps/                  # Map data files
├── maps/
│   ├── ADD_DerivedLowresBasemap.shp  # Shapefile for map generation
│   └── [Generated maps will be stored here]
├── scripts/
│   ├── generate_maps.py        # Script for generating maps
│   └── data1/                  # Temporary directory for data processing
├── .github/
│   └── workflows/
│       └── update_maps.yml     # GitHub Actions workflow for automated updates
├── README.md                   # This README file
└── netlify.toml                # (If still using Netlify for additional deployments)
```

## Updating the Website

When updating the website, consider the following:

1. **Dependencies:**
   Ensure that your Node.js and npm versions are up to date. Run `npm install` to update any outdated packages.

2. **CSS and JS:**
   Static assets such as CSS and JavaScript files are located in the `css/` and `js/` directories. Update these files as needed for styling and functionality changes.

3. **HTML Templates:**
   The main HTML files (`index.html`, `maps.html`, `csvs.html`, `about.html`) contain the structure and content of the website. Update these files for content changes.

## Automated Updates

The website's data and maps are automatically updated daily through a GitHub Actions workflow. This workflow:

1. Downloads the latest GeoPackage data.
2. Runs the `generate_maps.py` script to regenerate maps.
3. Commits the updated maps to the `maps` directory.
4. Deploys the changes to the `gh-pages` branch, updating the live site.

This automation ensures that the website always displays the most recent data.

## Troubleshooting

### Common Issues

1. **Deployment Failures:**
   If deployment to GitHub Pages fails, check the Actions tab in the GitHub repository for logs and errors.

2. **Broken Links or Assets:**
   Verify that all links and asset paths are correct. Use absolute paths where necessary to avoid issues with relative paths.

3. **Map Generation Errors:**
   Ensure that the `generate_maps.py` script runs correctly by testing it locally. Check for any issues with the GeoPackage data or shapefile.

## Acknowledgements

- [Bootstrap](https://getbootstrap.com/)
- [GitHub Pages](https://pages.github.com/)
- [GeoPandas](https://geopandas.org/)
- [Matplotlib](https://matplotlib.org/)

## Future Updates

If you are revisiting this project after some time, consider the following:

- **Check for Dependency Updates:** Run `npm outdated` to see if any dependencies need to be updated.
- **Review Documentation:** Revisit the Bootstrap and GitHub Pages documentation for any updates or new features.
- **Backup Data:** Ensure that you have backups of any critical data before making major changes.

## Contact

For further assistance, please contact Nathan Bekele at [nathanbek@outlook.com](mailto:nathanbek@outlook.com).
