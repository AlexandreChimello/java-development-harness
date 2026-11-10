
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


class TestCreateProject(unittest.TestCase):
# setUp executa antes dos testes e cria um ambiente temporário, copiando o gerador e template para lá
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)

        self.root = Path(self.temp.name)
        repository = Path(__file__).resolve().parent.parent

        (self.root / "scripts").mkdir()

        shutil.copy2(
            repository / "scripts" / "create_project.py",
            self.root / "scripts" / "create_project.py"
        )

        shutil.copytree(
            repository / "templates" / "java-basic",
            self.root / "templates" / "java-basic",
            ignore=shutil.ignore_patterns("target", ".idea", "*.iml")
        )

    def run_generator(self, *args):
        return subprocess.run(
            [
                sys.executable,
                str(self.root / "scripts" / "create_project.py"),
                *args
            ],
            capture_output=True,
            text=True
        )
# verifica se o projeto é criado com os arquivos corretos
    def test_creates_project(self):
        result = self.run_generator("calculadora")
# estilo o assertEquals do JUnit
        self.assertEqual(result.returncode, 0)

        project = self.root / "generated" / "calculadora"

        self.assertTrue((project / "pom.xml").exists())
        self.assertTrue(
            (project / "src/main/java/com/example/App.java").exists()
        )
        self.assertTrue(
            (project / "src/test/java/com/example/AppTest.java").exists()
        )

        pom = (project / "pom.xml").read_text(encoding="utf-8")
        self.assertIn("<artifactId>calculadora</artifactId>", pom)

# verifica se a harness impede nomes duplicados
    def test_rejects_duplicate_name(self):
        self.run_generator("calculadora")
        result = self.run_generator("calculadora")

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("já existe", result.stdout)
# verifica se harness verifica nomes com caracteres inválidos
    def test_rejects_invalid_name(self):
        result = self.run_generator("MeuProjeto")

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Erro:", result.stdout)
# verifica se o nome do projeto é obrigatório
    def test_requires_project_name(self):
        result = self.run_generator()

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Uso:", result.stdout)


if __name__ == "__main__":
    unittest.main()
