import os
import requests
import json
from datetime import datetime

# ========================================================
# ⚙️ API 연결 기본 검증 스크립트
# 목표: 환경변수 기반의 API 연결 및 JSON 데이터 파싱 능력 확인
# ========================================================

def check_api_connectivity(endpoint_url):
    """
    주어진 엔드포인트에 GET 요청을 보내 연결성을 테스트합니다.
    """
    print(f"[{datetime.now().strftime('%H:%M:%S')}] 🔗 API 연결 테스트 시작: {endpoint_url}")
    
    try:
        # 헤더에 임시 API 키를 포함시켜 실제 환경과 유사하게 만듭니다.
        # 실제 프로젝트에서는 os.getenv("NAVER_CLIENT_ID") 등을 사용합니다.
        headers = {
            "Content-Type": "application/json",
            "X-API-Test-Key": os.getenv("DUMMY_API_KEY", "TEST_SUCCESS")
        }
        
        # 타겟 API 호출 (공개 테스트용 JSONPlaceholder 사용)
        response = requests.get(endpoint_url, headers=headers, timeout=10)
        response.raise_for_status() # 200 코드가 아니면 예외 발생
        
        data = response.json()
        
        print("\n✅ API 연결 성공:")
        print(f"   상태 코드: {response.status_code}")
        print("   데이터 수신 성공. 일부 데이터 미리보기:")
        # 데이터가 리스트 형태일 경우 첫 항목을 출력합니다.
        if isinstance(data, list) and data:
            print(json.dumps(data[0], indent=2, ensure_ascii=False))
        else:
            print(json.dumps(data, indent=2, ensure_ascii=False))
            
    except requests.exceptions.RequestException as e:
        print(f"\n❌ API 연결 실패: {e}")
        print("   -> 네트워크 또는 API 인증/경로에 문제가 있을 수 있습니다.")
    except json.JSONDecodeError:
        print("\n❌ 데이터 파싱 실패: 응답이 유효한 JSON 형식이 아닙니다.")
    except Exception as e:
        print(f"\n❌ 알 수 없는 오류 발생: {e}")

if __name__ == "__main__":
    # 테스트용 공개 API 엔드포인트 (가짜 사용자 리소스)
    TEST_API_ENDPOINT = "https://jsonplaceholder.typicode.com/posts/1"
    check_api_connectivity(TEST_API_ENDPOINT)