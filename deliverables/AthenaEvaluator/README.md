# AthenaEvaluator

O AthenaEvaluator avalia conjuntos de dados de tráfego de rede a partir de metadados RDF. A ferramenta combina testes FAIR com métricas específicas de cibersegurança e apresenta os resultados em gráficos e tabelas.

## Funcionalidades

- Avaliar um conjunto de dados informando a URL do seu registro de metadados.
- Executar testes FAIR para avaliar se os dados são encontráveis, acessíveis, interoperáveis e reutilizáveis.
- Calcular métricas de cibersegurança, como atualidade, disponibilidade, anonimização, rotulagem, diversidade de ataques e completude da rede.
- Consultar avaliações anteriores no catálogo do Fair Data Point e, com as permissões necessárias, atualizar os metadados do conjunto de dados.

## Estrutura do projeto

- `client/` — interface web em Next.js, React e TypeScript.
- `server/` — API em Python e Flask que processa metadados RDF, executa os testes FAIR e calcula as métricas de cibersegurança.

## Como executar localmente

Use Python 3.11 e Node.js 22 com npm, as versões adotadas pelos Dockerfiles do projeto. Execute os comandos abaixo a partir da raiz do repositório, em dois terminais.

### 1. Iniciar a API

```bash
cd server
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python index.py
```

No Windows PowerShell, crie o ambiente com `py -3.11 -m venv .venv` e ative com `.\.venv\Scripts\Activate.ps1`.

Por padrão, a API fica disponível em `http://localhost:3001`. Para usar outra porta, configure a variável `PORT` e ajuste a URL da API no cliente.

### 2. Iniciar a interface web

No segundo terminal, entre em `client/` e crie o arquivo `client/.env.local` com o seguinte conteúdo:

```dotenv
NEXT_PUBLIC_SERVER_URL=http://localhost:3001
```

Em seguida, execute:

```bash
npm ci
npm run dev
```

Abra [http://localhost:3000](http://localhost:3000) no navegador.

## Como usar

1. Na página inicial, selecione **Evaluate dataset**.
2. Informe a URL de um registro acessível em RDF no formato Turtle, com um recurso do tipo `dcat:Dataset`.
3. Execute a avaliação e consulte as pontuações FAIR e de cibersegurança.
4. Para consultar avaliações anteriores, volte à página inicial e selecione **Analyze evaluations**.

A listagem de avaliações depende do catálogo do Fair Data Point. Os testes FAIR e a consulta de citações também dependem de serviços externos, portanto esses fluxos precisam de acesso à internet.

## Endpoints da API

| Método e rota | Entrada JSON | Resultado |
| --- | --- | --- |
| `POST /evaluate` | `dataset` com o conteúdo RDF em Turtle e `doi` opcional | Pontuações de cibersegurança, metadados e gráfico em PNG codificado em Base64. |
| `POST /proxy` | `subject` com a URL dos metadados e `tests` com a lista de identificadores dos testes FAIR | Resultados individuais dos testes, pontuações agregadas e parâmetros extraídos dos metadados. |
