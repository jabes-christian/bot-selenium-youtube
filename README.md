# 🎯 Automação Simples com Selenium: Pesquisa e Acesso a Vídeo no YouTube

Este repositório contém um **exemplo introdutório de automação com Selenium em Python**, com foco em navegação e interação com a interface do YouTube. A automação realiza os seguintes passos:

1. Acessa o site do YouTube.
2. Pesquisa por um termo específico.
3. Rola a página até encontrar um vídeo com o nome desejado.
4. Clica automaticamente no vídeo.

> 💡 Esta automação é ideal para quem está começando com Selenium e quer entender como localizar elementos, digitar, clicar e lidar com carregamentos dinâmicos em páginas web.

---

## 🚀 Tecnologias Utilizadas

- [Python 3.x](https://www.python.org/)
- [Selenium](https://pypi.org/project/selenium/)
- WebDriver (ChromeDriver recomendado)

---

## 📦 Instalação

### 1. Clone este repositório

```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
```

### 2. Acesse a pasta do projeto

```
cd nome-do-repositorio
```

### 3. Instale as dependências

```
pip install selenium

```
### 4. Baixe o ChromeDriver

Baixe o ChromeDriver compatível com a sua versão do Google Chrome:

https://chromedriver.chromium.org/downloads

Depois de baixar, adicione o executável do ChromeDriver ao PATH do seu sistema ou coloque-o na mesma pasta do script.

## ▶️ Como Executar

```
python nome_do_arquivo.py
```
| O script abrirá uma janela do Chrome, fará uma pesquisa no YouTube e clicará no primeiro vídeo”.

## 📚 Aprendizados

- Uso de XPATH para localizar elementos.
- Scroll dinâmico com JavaScript.
- Esperas explícitas com WebDriverWait.
- Manipulação básica de elementos com Selenium.

## 📌 Observações

- O script depende da estrutura atual do YouTube e pode precisar de ajustes caso o site seja atualizado.
- Para melhor desempenho, evite executar com múltiplas abas abertas no navegador.
- Este projeto é apenas para fins educacionais.

## 📄 Licença
Este projeto está licenciado sob a licença MIT.

## ✍️ Autor
Feito por **Jabes Christian** com fins educacionais e de prática com automação.
