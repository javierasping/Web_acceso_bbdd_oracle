# Pagina dinámica usa flask con acceso a oracle

Cuenta con una pagina de inicio y otra de obras , cuando accedas a esta ultima tendrás que rellenar un formulario para poder acceder a ver las tablas de ese usuario .

app_vulnerable.py --> Vulnerable a sqli Usuario:' OR '1'='1' -- contraseña:*
app_no_vulnerable.py --> Misma que la app_vulnerable.py pero sin ser vulnerable

app.py --> código que lista todas las tablas de un usuario de oracle 



Esquema de tablas utiliza la de mi proyecto del teatro de bbdd del año pasado . 

Cuenta con una tabla usuarios:

```
SQL> select * from usuarios;

USUARIO
--------------------------------------------------
CONTRASENA
--------------------------------------------------------------------------------
javi
javi
```

Video app vulnerable --> https://youtu.be/Vzu8xDOOiMU
Video app no vulnerable --> https://youtu.be/vK-R2_vB32U

## Bibliografía
[Authentication Bypass using SQL Injection on Login Page](https://www.geeksforgeeks.org/authentication-bypass-using-sql-injection-on-login-page/)
[SQL Injection in Python](https://knowledge-base.secureflag.com/vulnerabilities/sql_injection/sql_injection_python.html#vulnerable-example)