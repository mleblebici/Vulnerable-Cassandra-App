Vulnerable application for Cassandra Query Language (CQL) Injection.

Check the research blog here: <https://www.invicti.com/blog/web-security/investigating-cql-injection-apache-cassandra/>

Run `docker-compose up` to start using the vulnerable application. It will be running on port 8000.

In order to exploit the vulnerability, use following values for username and password.

Username: `admin'/*`

Password: `*/ and password >'`
