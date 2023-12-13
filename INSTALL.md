# URY Mosaic Installation

**Prerequisite Setup:**
- Before using URY Mosaic, ensure you have URY installed.
- Follow the [URY installation guide](https://github.com/ury-erp/ury/blob/main/INSTALLATION.md) for the installation process.

### To install URY Mosaic, follow these steps:

**Create New Site:**

```sh
  $ bench new-site sitename
```
**Install the URY Mosaic app to your bench:**

```sh
  $ bench get-app ury_mosaic https://github.com/ury-erp/mosaic.git
```
**To install URY Mosaic into site:**

```sh
  $ bench --site sitename install-app ury_mosaic
```

**Migrate the site:**

```sh
  $ bench --site sitename migrate
```