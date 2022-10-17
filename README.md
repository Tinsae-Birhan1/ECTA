## Install ECTA App with Bench CLI

1. Initialize frappe bench and install app
```bash
bench get --init-bench https://github.com/NATILEMMA/ECTA
```
2. Create new site 

```bash
bench new-site [your-sitename]
```
3. Install `ecta_dispatch` app on your site
```bash 
bench --site [your-sitename] install-app ecta_dispatch
```
4. Start app
```bash
bench start
```
