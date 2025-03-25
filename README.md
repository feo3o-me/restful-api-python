## Um programa simples para testar uma API restful.
## Usado *Postman* para testes.

Se receber o aviso **"Authorization failed"** vá para Headers e adicione "Authorization" com o **value** "1234".

Métodos
```
test()
add_user()
get_user_by_email()
search_user_by_domain()
```

Como usar:
```
http://localhost:1234/test
Retorna "OK" para sinalizar que a conexão está funcionando.
```
```
["POST"] -> Body -> raw
http://localhost:1234/user
Inserir os parâmetros ["email", "name", "password"]
Se o usuário já existir ele retornará "USER ALREADY EXISTS"
```
```
http://localhost:1234/email/<nome>
Retorna o email do usuário digitado, se existir.
Caso não exista retornará "USER NOT FOUND". 404
```
```
http://localhost:1234/search?email_domain=<dominio>
Retorna os usuários com o tipo de domínio de email selecionado. Ex: gmail.com
