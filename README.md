# Serverless Pipenv Starter with Plugin

A Pipenv starter project for [Serverless Framework](https://serverless.com/framework/) with [serverless-python-requirements plugin](https://github.com/UnitedIncome/serverless-python-requirements).

### Requirements

- [Install Python](https://www.python.org/downloads/)
- [Install the Serverless Framework](https://serverless.com/framework/docs/providers/aws/guide/installation/)
- [Configure your AWS CLI](https://serverless.com/framework/docs/providers/aws/guide/credentials/)

### Installation

Create a new project

```sh
$ serverless install --url https://github.com/seed-run/serverless-pipenv-starter --name serverless-pipenv-starter
```

Install Serverless plugin: serverless-python-requirements

```sh
$ npm install
```

### Usage

Run tests

```sh
$ pipenv run test
```

Invoke a function locally

```sh
$ serverless invoke local -f hello
```

### Deploying

Deploy your project

```sh
$ serverless deploy
```

Deploy a single function

```sh
$ serverless deploy function --function hello
```

### Support

- Send us an [email](mailto:frank@seed.run) if you have any questions
- Open a [new issue](https://github.com/seed-run/serverless-pipenv-starter/issues/new) if you've found a bug or have some suggestions.
- Or submit a pull request!

### Maintainers

Maintained by [Anomaly Innovations](https://anoma.ly/). [**Subscribe to our newsletter**](http://eepurl.com/cEaBlf) for updates. Send us an [email](mailto:contact@anoma.ly) if you have any questions.

