import time
import os
import shutil
import subprocess
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

logging.basicConfig(level=logging.INFO)

def regenPDF(path):
    FileName = str(path.src_path)
    FileName = FileName.replace('./target/', "")
    FileName = FileName.replace(".pdf", "")
    # logging.info("Nome do arquivo " + FileName)
    time.sleep(3)
    logging.info('gs -o "' + FileName + '_repaired.pdf" -sDEVICE=pdfwrite -dPDFSETTINGS=/prepress "./target/' + FileName + '.pdf"')
    command = 'gs -o "./data/' + FileName + '_repaired.pdf" -sDEVICE=pdfwrite -dPDFSETTINGS=/prepress "./target/' + FileName + '.pdf"'
    # command = ["echo", "Teste"]
    processo = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    # Lendo a saída linha por linha
    logging.info("Executando comando...")
    while True:
        linha = processo.stdout.readline()
        if linha == "" and processo.poll() is not None:
            break  # Sai do loop quando o processo terminar
        if linha:
            logging.info(linha.strip())  # Exibe a saída em tempo real

        # Verifica se houve erros no comando
        stderr = processo.stderr.read()
        if stderr:
            logging.info(f"Erro: {stderr}")


class MonitoramentoHandler(FileSystemEventHandler):
    def on_created(self, event):
        logging.info(f"Arquivo criado: {event.src_path}")
        regenPDF(event)

    # def on_modified(self, event):
    #     logging.info(f"Arquivo modificado: {event.src_path}")

    def on_deleted(self, event):
        logging.info(f"Arquivo deletado: {event.src_path}")

    def on_moved(self, event):
        logging.info(f"Arquivo movido de {event.src_path} para {event.dest_path}")

def verificar_pasta(caminho):
    """Verifica se o diretório existe e tem permissão."""
    if not os.path.exists(caminho):
        logging.info(f"Erro: O diretório {caminho} não existe.")
        return False
    if not os.access(caminho, os.R_OK):
        logging.info(f"Erro: Sem permissão de leitura no diretório {caminho}.")
        return False
    return True

def adicionar_tarefa_cron():
    # Obter o caminho absoluto do script atual
    caminho_script = os.path.abspath(__file__)

    # Comando cron que será agendado (todos os dias às 00:00)
    comando_cron = f"0 0 * * * /usr/bin/python3 {caminho_script}\n"

    # Lê as tarefas existentes no crontab
    processo = subprocess.Popen("crontab -l", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = processo.communicate()

    # Verifica se há crontab existente ou se precisa criar do zero
    if "no crontab" in stderr:
        tarefas_existentes = ""
    else:
        tarefas_existentes = stdout

    # Adiciona a nova tarefa ao final das tarefas existentes
    novas_tarefas = tarefas_existentes + comando_cron

    # Salva as tarefas atualizadas no crontab
    processo = subprocess.Popen("crontab -", shell=True, stdin=subprocess.PIPE, text=True)
    processo.communicate(novas_tarefas)

    logging.info(f"Tarefa agendada com sucesso! O script será executado todos os dias às 00:00.")


if __name__ == "__main__":
    adicionar_tarefa_cron()
    caminho = "./target"  # Altere para o caminho da sua pasta

    if verificar_pasta(caminho):
        event_handler = MonitoramentoHandler()
        observer = Observer()
        observer.schedule(event_handler, caminho, recursive=True)

        logging.info("Monitorando a pasta...")
        observer.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
            logging.info("Monitoramento encerrado.")

        observer.join()