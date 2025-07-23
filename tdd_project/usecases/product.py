from motor.motor_asyncio import AsyncIOMotorClient
from uuid import UUID
from tdd_project.db.mongo import db_client
from tdd_project.schemas.product import ProductIn, ProductOut


class ProductUsecase:
    def __init__(self) -> None:
        self.client: AsyncIOMotorClient = db_client.get()
        self.database = self.client.get_database()
        self.collection = self.database.get_collection("products")

    async def create(self, body: ProductIn) -> ProductOut:
        product = ProductOut(**body.model_dump())
        await self.collection.insert_one(product.model_dump())

        return product

    async def get(self, id: UUID) -> ProductOut:
        result = await self.collection.find_one({"id": id})

        return ProductOut(**result)


product_usecase = ProductUsecase()
