# URY Mosaic Installation

**Prerequisite Setup:**
- Before using URY Mosaic, ensure you have URY installed.
- Doppio is used to setup and manage  custom desk pages using Vue 3 on URY Mosaic App and you don't have to install doppio in your site.
- Follow the [URY installation guide](https://github.com/ury-erp/ury/blob/main/INSTALLATION.md) for the installation process.

### To install URY Mosaic, follow these steps:

**Create New Site:**

```sh
  $ bench new-site sitename
```

**Install the Doppio app to your bench:**

```sh 
  $ bench get-app https://github.com/NagariaHussain/doppio
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