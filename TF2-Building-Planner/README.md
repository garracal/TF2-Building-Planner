# TF2 Building Planner

A free, in-browser tool for planning engineer buildings on top-down Team Fortress 2 maps, with a library of configs shared by the community.

**Use it:** https://YOUR-USERNAME.github.io/YOUR-REPO/

Everything you make is saved in your own browser. Nothing is uploaded anywhere unless you share a config.

## Share a config

1. In the planner, open **Export / Import → Export JSON…**, confirm the title, author and short description, and save the file.
2. Open the `configs` folder in this repository, then the folder for your map (or create one).
3. Choose **Add file → Upload files** and drop your `.json` in. GitHub will offer to create a fork and a pull request for you. Files up to 25 MB can be uploaded this way.
4. Fill in the pull request form and submit it. Once it is reviewed and merged, your config appears in the in-app **Library** within a couple of minutes.

## Use a config from the library

Open **Library**, find a config and click **Add to my maps**. It becomes a normal map in your browser that you can edit.

## Run it on your own computer

You need Python 3. Put the files in one folder and double-click `start-library.bat` (Windows) or `start-library.command` (Mac/Linux). It rebuilds the library index and opens the site at http://localhost:8000/.

## Notes

- Team Fortress 2 and its artwork, icons and fonts are the property of Valve. This is an unofficial fan project and is not affiliated with Valve.
