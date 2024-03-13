import flask

from chapter1.model import OrderLine

# Psudocode
@flask.route.gubbins
def allocate_endpoint():
    # 요청으로부터 주문라인 추출
    line = OrderLine(request.params..)
    # DB에서 모든 배치 가져오기
    batchs = None
    # 도메인 서비스 호출
    allocate(line, batches)
    # 어떤 방식으로든 할당한 배치를 다시 데이터베이스에 저장
    return 201
