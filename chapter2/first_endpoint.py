import flask

from chapter1.model import OrderLine

# Psudocode
@flask.route.gubbins
def allocate_endpoint():
    session = start_session()

    # 요청애서 주문라인을 추출
    line = OrderLine(
        request.json['orderId'],
        request.json['sku'],
        request.json['qty'],
    )

    # DB에서 모든 배치를 가져온다
    batches = session.query(Batch).all()

    # 도메인 서비스를 호출한다
    allocate(line, batches)

    # 할당온 데이터베이스에 저장한다
    session.commit()

    return 201
