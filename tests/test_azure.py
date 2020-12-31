import pytest
import asyncio

from tools.azure_sub import azure_sub


@pytest.mark.asyncio
async def test_azure_001():
    await azure_sub()
    assert '{"msg":"this is just a test"}' == pytest.message