# Indonesia Village Cascade Generator

In (Akvo Flow)[http://flowsupport.akvo.org/], the cascade questions are based on a cascade resource. Once you create the cascade resource you can reuse it limitlessly in any number of cascade questions in any survey. Creating one cascade resource allows you to use one resource multiple times without having to duplicate the work. This repository is example to generate Akvo Flow cascade resources automatically. 

### Requirements

- Python 3 or Above 
- Virtualenv (Recommended) or Miniconda or Anaconda (Optional)

### Installation

- Clone the repository
```
$ git clone https://github.com/dedenbangkit/indo-village-cascade
```

- Create Virtual ENV with venv 
```
// Using Virtualenv
$ virtualenv -p /usr/bin/python3.7 ENV_NAME 

// Using Conda
$ conda create -n ENV_NAME python=3.7 anaconda
```

- Activate the ENV
```
$ source ENV_NAME/bin/activate
```

- Install Requirements
```
// Using PIP
$ pip install -r requirements.txt

// Using Conda
$ conda install --yes --file requirements.txt
```

### Listing The Resources

See ```runner.sh``` to see how it works.
