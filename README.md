# Cloud Computing Project

### Author: Bernardo Cunha Capoferri
### Course: Engenharia da computação
### year: 2022
<br/>

## Description
This is a simple **CLI** program coded using **Python** to create an *Amazon Web Service* (AWS) infrastructure using the *Infrastructure as Code* (IaC) language **Terraform**. It's objective was to simplify the process of Creating and deleting:
- EC2 instances
- security groups and their rules.
- IAM Users
- High-Availability systems

In two AWS regions *us-east-1* and *us-east-2*
<br/>

## Rquirements

<br/>

### OS:
The program was coded and tested on **Ubuntu 22.04.1**, it's recommended to use a Linux OS with this code.
<br/>

### Terraform:
It is necessary that the IaC **Terraform** version 1.3.5 or above be installed in your system.

To install it, follow the [tutorial](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli) in HashiCorp's website.
<br/>

### Python:
It's reccommended that version 3.10.6 or above be installed.

<br/>

## Configuring enviroment variables in Linux
**Terraform** requires access keys to authorize it to realize alteration in your AWS cloud, they are obtained when creating a user with resource creation permissions. There exists two options to give terraform this information:
- Put the keys in your local enviroment by running the following commands in your terminal:
```sh
$ export AWS_ACCESS_KEY_ID= <SUA_ACCESS_KEY>
$ export AWS_SECRET_ACCESS_KEY= <SUA_SECRET_ACCESS_KEY>
```
Be aware that this is a temporary measure and will only be available in the current session.

- A more permanent option puts the previous commands in the `.bashrc` file and running the following command to update the open terminal:
```sh
$ source ~/.bashrc
```
<br>

## How to run the code
First, clone the repository
```sh
$ git clone git@github.com:bert799/ProjetoCompNuvem.git # Clone com SSH (recomendado)
$ git clone https://github.com/bert799/ProjetoCompNuvem # Clone com HTTPS
```
With your terminal open enter the folder `python/` and run the following command:
```sh
$ python3 projeto.py
```
All done! Now all you need to do is follow the CLI menus to construct your infrastructure.  

## Project guide (Portuguse-BR)

Can be found on this link [site](https://bert799.github.io/roteiro-proj-CompNuvem/), also contains a **Terraform** tutorial