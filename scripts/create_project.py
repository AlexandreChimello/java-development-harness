from pathlib import Path
import re
import shutil
import sys


def main():
    if len(sys.argv) != 2:
        print("Uso: python scripts/create_project.py nome-do-projeto")
        return 1

    project_name = sys.argv[1]

    if not re.fullmatch(r"[a-z][a-z0-9]*(?:-[a-z0-9]+)*", project_name):
        print("Erro: use letras minúsculas, números e hífens.")
        return 1

    root = Path(__file__).resolve().parent.parent
    template = root / "templates" / "java-basic"
    destination = root / "generated" / project_name

    if destination.exists():
        print(f"Erro: o projeto '{project_name}' já existe.")
        return 1

    pom_content = (template / "pom.xml").read_text(encoding="utf-8")
    original_name = "<artifactId>java-basic</artifactId>"

    if original_name not in pom_content:
        print("Erro: o template Maven não possui o artifactId esperado.")
        return 1

    destination.parent.mkdir(parents=True, exist_ok=True)

    shutil.copytree(
        template,
        destination,
        ignore=shutil.ignore_patterns("target", ".idea", "*.iml")
    )

    new_pom = pom_content.replace(
        original_name,
        f"<artifactId>{project_name}</artifactId>",
        1
    )

    (destination / "pom.xml").write_text(new_pom, encoding="utf-8")

    print(f"Projeto '{project_name}' criado com sucesso!")
    return 0


if __name__ == "__main__":
    sys.exit(main())
