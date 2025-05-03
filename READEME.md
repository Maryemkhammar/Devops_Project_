# devops-project
# DevOps Project – Déploiement d’une Application Web avec CI/CD et Docker

##  Objectif
Ce projet a pour objectif de :
- Créer une application web simple avec Flask.
- La conteneuriser avec Docker.
- Mettre en place une pipeline CI/CD via GitHub Actions.
- Déployer et gérer l’application localement avec Terraform (Infrastructure as Code).

---

##  Technologies utilisées
- **Python / Flask**
- **Docker**
- **Git / GitHub**
- **GitHub Actions** (CI/CD)
- **Terraform**
- **Pytest** (tests unitaires)

---

## Lancer l'application
# En local (hors Docker)
 python app.py

# Avec Docker
```bash
 docker build -t myapp .
 docker run -p 5000:5000 myapp
```

# Avec Terraform
```bash
 terraform init
 terraform apply
```

# Remarque
 Un runner GitHub auto-hébergé a été utilisé pour le déploiement local.