# Chatbot HEMOBA

Este é um projeto acadêmico onde foi criado um chatbot para responder perguntas relacionadas ao HEMOBA (Hemocentro de Vitória da Conquista). Ele fornece informações sobre localização, horários de funcionamento, requisitos para doação de sangue, como acessar resultados de exames e documentos necessários para doação.

## Requisitos
Antes de executar o chatbot, verifique se você possui os seguintes itens instalados:

- Python 
- Gerenciador de pacotes `pip`
- Node

## Instalação

1. Instale as dependências necessárias:
   ```terminal
   pip install -r requirements.txt
   ```

## Como Executar
1. Realize o treinamento:
   ```terminal
   python treinamento.py
   ```
2. Inicie o serviço:
   ```terminal
   python servico.py
   ```
3. Navegue até pasta chat e inicie o index.js:
    ```terminal
    cd chat
   node index.js
   ```
4. Acesse o endereço por um navegador web: 
   ``` 
   http://localhost:3000 
   ```
## Exemplo de Uso
Quando iniciado, o chatbot pode responder perguntas como:

- "Onde fica o HEMOBA?"
- "Qual o horário de funcionamento?"
- "Quem pode doar sangue?"
- "Onde consigo ver o resultado do meu exame?"
- "Quais documentos sao necessarios?"

O chatbot irá fornecer respostas baseadas nas informações cadastradas.