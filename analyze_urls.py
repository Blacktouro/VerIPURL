import socket
from urllib.parse import urlparse, parse_qs

def get_ip_from_url(full_url):
    try:
        parsed_url = urlparse(full_url)
        domain = parsed_url.netloc if parsed_url.netloc else parsed_url.path
        ip = socket.gethostbyname(domain)
        return ip
    except socket.gaierror as e:
        return f"Erro ao resolver o domínio: {e}"

def analyze_url(url):
    parsed_url = urlparse(url)
    path = parsed_url.path
    params = parse_qs(parsed_url.query)
    return path, params

# URLs para verificar
urls = [
    "https://17577-2.ep.egorealestate.com/es-es/promociones?catids=148&pag=1&srt=1&wvstest=javascript:domxssExecutionSink(1,\"'\"><xsstag>()locxss\")",
    "https://11386-2.ep.egorealestate.com/equipa?aos=undefined&gather_attributes=undefined&pag=undefined&thumbnailsize={{41007*41007}}",
    "/virtual/PrintProperty.aspx?lng=es-es&prop=19917769&token=\";print(md5(31337));%24a=\"",
    "/virtual/PrintProperty.aspx?lng=en-gb&prop=19917769&token=HttP://bxss.me/t/xss.html%3F%2500",
    "https://17577-2.ep.egorealestate.com/en-gb/miamiproperties/cleveland,detroit,-1' OR 2+33-33-1=0+0+0+1 --"
]

# Domínio base para URLs relativas
base_domain = "https://example.com"

# Iterar sobre cada URL e imprimir o IP e parâmetros
for url in urls:
    if url.startswith('/'):
        full_url = base_domain + url  # Adiciona domínio base para URLs relativas
    else:
        full_url = url
    
    ip = get_ip_from_url(full_url)
    path, params = analyze_url(full_url)
    
    print(f"O IP do URL {url} é: {ip}")
    print(f"Path: {path}")
    print(f"Parâmetros: {params}\n")

