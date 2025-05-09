from typing import List
from app.common.exceptions.product_exceptions import ProductNotFoundError, InvalidProductInputError
from app.common.utils.normalize import normalize_text
from app.common.utils.load_data import load_data
from app.models.product import Product

def get_all() -> List[Product]:
    all_products = load_data()
    filtered = []
    for product in all_products:
        filtered.append({
            "id": product["id"],
            "nombre": product["name"],
            "tipo": product["type"],
            "descripcion": product["description"],
            "meses": product["months"],
            "regiones": product["regions"],
            "imagen": product["image"],
        })
    return filtered

def get_product_by_id(id: int) -> Product:
    if id < 1 or not isinstance(id, int):
        raise InvalidProductInputError("Invalid ID.")
    all_products = load_data()
    for product in all_products:
        if product["id"] == id:
            return {
                "id": product["id"],
                "nombre": product["name"],
                "tipo": product["type"],
                "descripcion": product["description"],
                "meses": product["months"],
                "regiones": product["regions"],
                "imagen": product["image"],
            }
        else:
            raise ProductNotFoundError(f"Product with ID {id} not found.")

def get_products(region: str, mes: str) -> List[Product]:
    all_products = load_data()
    region = normalize_text(region)
    mes = normalize_text(mes)
    filtered = []
    for product in all_products:
        if region.lower() in [normalize_text(r) for r in product["regions"]] and mes.lower() in [normalize_text(m) for m in product["months"]]:
            filtered.append({
                "id": product["id"],
                "nombre": product["name"],
                "tipo": product["type"],
                "descripcion": product["description"],
                "meses": product["months"],
                "regiones": product["regions"],
                "imagen": product["image"],
            })
    return filtered

def get_products_by_type(tipo: str) -> List[Product]:
    all_products = load_data()
    filtered = []
    for product in all_products:
        if tipo.lower() in product["type"].lower():
            filtered.append({
                "id": product["id"],
                "nombre": product["name"],
                "tipo": product["type"],
                "descripcion": product["description"],
                "meses": product["months"],
                "regiones": product["regions"],
                "imagen": product["image"],
            })
    return filtered