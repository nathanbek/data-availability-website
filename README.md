# QIceRadar Website

## Overview

The QIceRadar website is designed to visualize and provide access to data collected by various institutions on Antarctic research. This website is built with HTML, CSS, JavaScript, and Bootstrap and is deployed on Netlify for easy and efficient deployment.

## Table of Contents

1. [Getting Started](#getting-started)
2. [Installation](#installation)
3. [Development](#development)
4. [Deployment](#deployment)
5. [Project Structure](#project-structure)
6. [Updating the Website](#updating-the-website)
7. [Troubleshooting](#troubleshooting)
8. [Acknowledgements](#acknowledgements)
9. [Future Updates](#future-updates)
10. [Contact](#contact)

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

The website is deployed on Netlify using the drag-and-drop feature. To deploy updates, follow these steps:

1. **Build the site:**
   Ensure your site is ready for deployment by building it. If you're using plain HTML, CSS, and JS, this step may simply involve ensuring all your files are up to date and correctly linked.

2. **Drag and drop the folder:**

   - Zip the contents of your project directory (the files you want to deploy, including `index.html`, `css`, `js`, `assets`, etc.).
   - Go to the Netlify dashboard.
   - Drag and drop the zip file into the Netlify site area.

3. **Update the site:**
   To update the site, repeat the drag-and-drop process with the updated files.

## Project Structure

Here's a brief overview of the project's structure:
qiceradar-website/
├── index.html # Home page
├── maps.html # Maps page
├── csvs.html # CSV Data page
├── about.html # About page
├── css/
│ └── styles.css # Custom styles
├── js/
│ └── scripts.js # Custom scripts
├── assets/
│ ├── images/ # Image assets
│ ├── csvs/ # CSV data files
│ └── maps/ # Map data files
├── README.md # This README file
└── netlify.toml # Netlify configuration file

## Updating the Website

When updating the website, consider the following:

1. **Dependencies:**
   Ensure that your Node.js and npm versions are up to date. Run `npm install` to update any outdated packages.

2. **CSS and JS:**
   Static assets such as CSS and JavaScript files are located in the `css/` and `js/` directories. Update these files as needed for styling and functionality changes.

3. **HTML Templates:**
   The main HTML files (`index.html`, `maps.html`, `csvs.html`, `about.html`) contain the structure and content of the website. Update these files for content changes.

## Troubleshooting

### Common Issues

1. **Deployment Failures:**
   If deployment to Netlify fails, ensure that all files are correctly linked and there are no syntax errors in your HTML, CSS, or JavaScript.

2. **Broken Links or Assets:**
   Verify that all links and asset paths are correct. Use absolute paths where necessary to avoid issues with relative paths.

## Acknowledgements

- [Bootstrap](https://getbootstrap.com/)
- [Netlify](https://www.netlify.com/)

## Future Updates

If you are revisiting this project after some time, consider the following:

- **Check for Dependency Updates:** Run `npm outdated` to see if any dependencies need to be updated.
- **Review Documentation:** Revisit the Bootstrap and Netlify documentation for any updates or new features.
- **Backup Data:** Ensure that you have backups of any critical data before making major changes.

## Contact

For further assistance, please contact Nathan Bekele at [nathanbek@outlook.com](nathanbek@outlook.com).

---

By providing comprehensive documentation in this README file, you'll help future developers (including future yourself) understand and maintain the project more effectively.
