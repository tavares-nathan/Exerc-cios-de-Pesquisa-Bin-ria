import requests

TOKEN = "5236a7abbb696469dcce3f574f672e23e23b6d523229c0489c8ae94ea7ec034a"

URL_BASE = "https://api.olhovivo.sptrans.com.br/v2.1"


def autenticar():
    url = f"{URL_BASE}/Login/Autenticar"

    try:
        resposta = requests.post(
            url,
            params={"token": TOKEN},
            timeout=15
        )

        print("Status HTTP:", resposta.status_code)
        print("Resposta da API:", resposta.text)

        resposta.raise_for_status()

        if resposta.text.strip().lower() == "true":
            print("Autenticação realizada com sucesso!")
            return resposta.cookies

        print("Não foi possível autenticar.")
        return None

    except requests.RequestException as erro:
        print(f"Erro na requisição: {erro}")
        return None


if __name__ == "__main__":
    cookies = autenticar()

    if cookies:
        print("Token autenticado e sessão iniciada.")