import flask

from chapter1.model import OrderLine
from repository import SqlAlchemyRepository

# Psudocode
@flask.route.gubbins
def allocate_endpoint():
    batches = SqlAlchemyRepository.list()
    lines = [
        OrderLine(l['orderId'],l['sku'],l['qty'])
        for l in request.params
    ]
    allocate(line, batches)
    # 할당온 데이터베이스에 저장한다
    session.commit()

    return 201
