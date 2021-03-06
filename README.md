# Como criar um ambiente de ICP para teste

- em IBM Cloud, execute o script abaixo em um computador com ansible instalado para criar os servidores de ICP
- edite o arquivo hosts.txt, para alterar os nomes dos hosts que serão criados.

## Pré-requisitos
- slcli instalado e configurado
- ansible instalado e configurado (incluíndo o módulo da Softlayer para ansible)

## Para criar os servidores 
- ansible-playbook -i hosts.txt create.yml 

## Para destruir os servidores
- ansible-playbook -i hosts.txt.destroy.yml

## Para instalar o ICP nos servidores criados
- faça login no servidor e execute
````
curl -l https://raw.githubusercontent.com/IBMCloudBrazil/criar_ambiente_icp/master/install.py | python
````

---------------------------------

## Usando o docker para criar os servidores 
- execute o container 
````
docker run -it jmbarros/icp-nodes:2.1.0.2 /bin/bash
`````
- configure o cli da IBM Cloud
````
slcli setup
````
- edite o arquivo hosts.txt e configure os hosts que vc quer
````
vim hosts.txt
````
- execute o playbook de instalação 
````
ansible-playbook -i hosts.txt create.yml
''''

