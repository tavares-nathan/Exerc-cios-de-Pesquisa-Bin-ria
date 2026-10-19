import requests

TOKEN = "9f4d1f2f53b5f131e2552c848ac28a13302a36f3f73cbe57153b381d928bf589"

URL_BASE = "https://api.olhovivo.sptrans.com.br/v2.1"


def autenticar():
    url = f"{URL_BASE}/Login/Autenticar"

    try:
        resposta = requests.post(
            url,
            headers={
                "Authorization": TOKEN
            },
            timeout=15
        )

        resposta.raise_for_status()

        if resposta.text.strip().lower() == "true":
            print("Autenticação realizada com sucesso!")
            return resposta.cookies

        print("Não foi possível autenticar.")
        print(resposta.text)
        return None

    except requests.RequestException as erro:
        print(f"Erro na requisição: {erro}")
        return None


if __name__ == "__main__":
    cookies = autenticar()

    if cookies:
        print("Token autenticado e sessão iniciada.")