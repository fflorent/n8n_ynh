<!--
N.B.: This README was automatically generated by https://github.com/YunoHost/apps/tree/master/tools/README-generator
It shall NOT be edited by hand.
-->

# n8n for YunoHost

[![Integration level](https://dash.yunohost.org/integration/n8n.svg)](https://dash.yunohost.org/appci/app/n8n) ![](https://ci-apps.yunohost.org/ci/badges/n8n.status.svg) ![](https://ci-apps.yunohost.org/ci/badges/n8n.maintain.svg)  
[![Install n8n with YunoHost](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=n8n)

*[Lire ce readme en français.](./README_fr.md)*

> *This package allows you to install n8n quickly and simply on a YunoHost server.
If you don't have YunoHost, please consult [the guide](https://yunohost.org/#/install) to learn how to install it.*

## Overview

n8n is an extendable workflow automation tool. With a fair-code distribution model, n8n will always have visible source code, be available to self-host, and allow you to add your own custom functions, logic and apps. n8n's node-based approach makes it highly versatile, enabling you to connect anything to everything.

**Shipped version:** 0.138.0~ynh1

**Demo:** https://demo.example.com

## Screenshots

![](./doc/screenshots/n8n-screenshot.png)

## Documentation and resources

* Official app website: https://n8n.io/
* Official admin documentation: https://docs.n8n.io/
* Upstream app code repository: https://github.com/n8n-io/n8n
* YunoHost documentation for this app: https://yunohost.org/app_n8n
* Report a bug: https://github.com/YunoHost-Apps/n8n_ynh/issues

## Developer info

Please send your pull request to the [testing branch](https://github.com/YunoHost-Apps/n8n_ynh/tree/testing).

To try the testing branch, please proceed like that.
```
sudo yunohost app install https://github.com/YunoHost-Apps/n8n_ynh/tree/testing --debug
or
sudo yunohost app upgrade n8n -u https://github.com/YunoHost-Apps/n8n_ynh/tree/testing --debug
```

**More info regarding app packaging:** https://yunohost.org/packaging_apps