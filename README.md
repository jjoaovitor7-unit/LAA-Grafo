# LAA-Grafo
## Como baixar e rodar o projeto?
* Para a versão do terminal:
  * Para grafo não-valorado:
    ```
    git clone https://github.com/jjoaovitor7-unit/LAA-Grafo
    cd LAA-Grafo
    pip3 install -r v2-terminal/requirements.txt
    python3 v2-terminal/nao-valorado.py
    ```

  * Para grafo valorado:
    ```
    git clone https://github.com/jjoaovitor7-unit/LAA-Grafo
    cd LAA-Grafo
    pip3 install -r v2-terminal/requirements.txt
    python3 v2-terminal/valorado.py
    ```

 <br />

* Para a versão da interface gŕafica:
  * Para grafo não-valorado:
    ```
    git clone https://github.com/jjoaovitor7-unit/LAA-Grafo
    cd LAA-Grafo
    pip3 install -r v3-gui/requirements.txt
    python3 v3-gui/nao-valorado.py
    ```
  * Para grafo valorado:
    ```
    git clone https://github.com/jjoaovitor7-unit/LAA-Grafo
    cd LAA-Grafo
    pip3 install -r v3-gui/requirements.txt
    python3 v3-gui/valorado.py
    ```

 <br />

* Para a versão web
  * Para grafo valorado e não-valorado:
  ```
  git clone https://github.com/jjoaovitor7-unit/LAA-Grafo
  cd LAA-Grafo/v4-web
  python3 -m http.server
  http://0.0.0.0:8000/
  ```