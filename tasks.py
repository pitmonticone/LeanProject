import os
import shutil
import subprocess
from pathlib import Path
from invoke import run, task

from blueprint.tasks import web, bp, print_bp, serve

# Define the root directory and blueprint directory paths
ROOT = Path(__file__).parent
BP_DIR = ROOT / 'blueprint'

@task(bp, web)
def all(ctx):
    """
    Task to clean and rebuild the documentation:
    1. Removes the existing 'docs/blueprint' directory if it exists.
    2. Copies the 'blueprint/web' directory to 'docs/blueprint'.
    3. Copies the 'blueprint/print/print.pdf' file to 'docs/blueprint.pdf'.
    """
    shutil.rmtree(ROOT / 'docs' / 'blueprint', ignore_errors=True)
    shutil.copytree(ROOT / 'blueprint' / 'web', ROOT / 'docs' / 'blueprint')
    shutil.copy2(ROOT / 'blueprint' / 'print' / 'print.pdf', ROOT / 'docs' / 'blueprint.pdf')

@task(web)
def html(ctx):
    """
    Task to rebuild the HTML documentation:
    1. Removes the existing 'docs/blueprint' directory if it exists.
    2. Copies the 'blueprint/web' directory to 'docs/blueprint'.
    """
    shutil.rmtree(ROOT / 'docs' / 'blueprint', ignore_errors=True)
    shutil.copytree(ROOT / 'blueprint' / 'web', ROOT / 'docs' / 'blueprint')

@task(bp, web)
def dev(ctx):
    """
    Task to serve the blueprint website and rebuild the PDF and website on file changes:
    1. Detects changes in the 'blueprint/src' directory.
    2. Calls the 'bp' and 'web' tasks to rebuild the PDF and website, respectively.
    3. Ignores specific temporary and output file patterns.
    """
    from watchfiles import run_process, DefaultFilter

    def callback(changes):
        """
        Callback function that is called when file changes are detected.
        """
        print('Changes detected:', changes)
        bp(ctx)
        web(ctx)
    
    run_process(BP_DIR / 'src', target='inv serve', callback=callback,
        watch_filter=DefaultFilter(
            ignore_entity_patterns=(
                '.*\.aux$',        # Ignore auxiliary files
                '.*\.log$',        # Ignore log files
                '.*\.fls$',        # Ignore fls files
                '.*\.fdb_latexmk$',# Ignore latexmk database files
                '.*\.bbl$',        # Ignore bibliography files
                '.*\.paux$',       # Ignore paux files
                '.*\.pdf$',        # Ignore pdf files
                '.*\.out$',        # Ignore out files
                '.*\.blg$',        # Ignore bibliography log files
                '.*\.synctex.*$',  # Ignore synctex files
            )
        ))