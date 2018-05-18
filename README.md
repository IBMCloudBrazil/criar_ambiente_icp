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