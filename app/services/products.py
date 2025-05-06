from typing import List
from app.utils.normalize import normalize_text
from app.utils.load_data import load_data
from app.models.product import Product

def get_all() -> List[Product]:
    all_products = load_data()
    filtered = []
    for product in all_products:
        filtered.append({
            "nombre": product["name"],
            "tipo": product["type"],
            "descripcion": product["description"],
            "meses": product["months"],
            "regiones": product["regions"],
            "imagen": product["image"],
        })
    return filtered

def get_products(region: str, mes: str) -> List[Product]:
    all_products = load_data()
    region = normalize_text(region)
    mes = normalize_text(mes)
    filtered = []
    for product in all_products:
        if region.lower() in [normalize_text(r) for r in product["regions"]] and mes.lower() in [normalize_text(m) for m in product["months"]]:
            filtered.append({
                "nombre": product["name"],
                "tipo": product["type"],
                "descripcion": product["description"],
                "meses": product["months"],
                "regiones": product["regions"],
                "imagen": product["image"],
            })
    return filtered
    
def get_product_by_type(tipo: str) -> List[Product]:
    all_products = load_data()
    if tipo.lower() == "all":
        return all_products
    tipo_normalizado = normalize_text(tipo)
    filtered = []
    for product in all_products:
        types_raw = product["type"]
        if isinstance(types_raw, str):
            types_raw = [types_raw]
        normalized_types = [normalize_text(t) for t in types_raw]
        print(f"Comparando {tipo_normalizado} con {normalized_types}")
        if tipo_normalizado in normalized_types:
            filtered.append({
                "nombre": product["name"],
                "tipo": product["type"],
                "descripcion": product["description"],
                "meses": product["months"],
                "regiones": product["regions"],
                "imagen": product["image"],
            })
    return filtered

def get_product_by_name(name: str) -> List[Product]:
    all_products = load_data()
    name_normalizado = normalize_text(name)
    filtered = []
    for product in all_products:
        if name_normalizado in [normalize_text(n) for n in product["name"]]:
            filtered.append({
                "nombre": product["name"],
                "tipo": product["type"],
                "descripcion": product["description"],
                "meses": product["months"],
                "regiones": product["regions"],
                "imagen": product["image"],
            })
    return filtered