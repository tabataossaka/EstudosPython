import xml.etree.ElementTree as ET

dados = """<?xml version='1.0' encoding='utf-8'?>
<clientes>
    <cliente>
        <id>1</id>
        <nome>Rodrigo</nome>
        <idade>30</idade>
        <cidade>BH</cidade>
    </cliente>
    <cliente>
        <id>2</id>
        <nome>Luna</nome>
        <idade>20</idade>
        <cidade>RJ</cidade>
    </cliente>
</clientes>
"""

caminho_arquivo = "clientes.xml"

# 1 - Exportando dados para XML
with open(caminho_arquivo, "w", encoding="utf-8") as file:
    file.write(dados)

# 2 - Lendo dados do XML
tree = ET.parse(caminho_arquivo)
root = tree.getroot()

# 3 - Percorrendo os clientes
for cliente in root.findall("cliente"):
    id_cliente = cliente.find("id").text
    nome_cliente = cliente.find("nome").text

    print(f"Id: {id_cliente} -> Nome: {nome_cliente}")


# Adicionando novo cliente
novo_cliente = ET.Element("cliente")

id_novo = ET.SubElement(novo_cliente, "id")
id_novo.text = "5"

nome_novo = ET.SubElement(novo_cliente, "nome")
nome_novo.text = "Carlos"

idade_novo = ET.SubElement(novo_cliente, "idade")
idade_novo.text = "25"

cidade_novo = ET.SubElement(novo_cliente, "cidade")
cidade_novo.text = "Campinas"

root.append(novo_cliente)

# Salvando no XML
tree.write(caminho_arquivo, encoding="utf-8", xml_declaration=True)