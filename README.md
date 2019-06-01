<div align="center">
  <img width="100" src="https://cdn.becauseofprog.fr/logos/bop-transparent.png"/>
  <h1>BecauseOfProg's website</h1>
  <h4>Production : <a href="https://becauseofprog.fr">becauseofprog.fr</a></h4>
  <h4>Development : <a href="https://beta.becauseofprog.fr">beta.becauseofprog.fr</a></h4>
  <img src="https://img.shields.io/badge/version-3.0--beta-yellow.svg"/>
</div>

## Installation

### Requirements

* Python 3.5+
* NodeJS 10+

### Project setup

* Clone the repository from git
* Install the Python dependencies : `pip install -r requirements.txt`
* Install the NodeJS dependencies : `npm i` or `yarn install`

## For development

* Run the Rollup development server : `npm run dev` or `yarn dev`
* Start the `run.py` script

## For production

* Compile the CSS and Javascript bundle : `npm run build` or `yarn build`
* Add a systemd service to serve the blog-old with uWSGI (a configuration file for uWSGI is included: site-bop-v3.ini)