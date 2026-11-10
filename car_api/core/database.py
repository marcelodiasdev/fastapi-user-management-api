from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from car_api.core.settings import Settings

# Motor de conexão assincrona -> Engineer de conexão
engine = create_async_engine(Settings().DATABASE_URL)


async def get_session():
    async with AsyncSession(engine, expire_on_commit=False) as session:
        yield session
