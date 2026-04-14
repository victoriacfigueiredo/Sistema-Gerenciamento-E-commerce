from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class AvaliacaoPedidoResponse(BaseModel):
    id_avaliacao: str
    id_pedido: str
    avaliacao: int
    titulo_comentario: Optional[str] = None
    comentario: Optional[str] = None
    data_comentario: Optional[datetime] = None
    data_resposta: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)