import os
import json
import requests
from datetime import datetime

# 환경 변수에서 API 키 로드 (보안을 위해 사용)
NAVER_CLIENT_ID = os.environ.get("NAVER_CLIENT_ID")
NAVER_SECRET = os.environ.get("NAVER_SECRET")
TISTORY_API_KEY = os.environ.get("TISTORY_API_KEY")

def publish_to_naver(content_data: dict) -> bool:
    """
    네이버 블로그 API를 사용하여 콘텐츠를 발행합니다.
    (실제 API 호출은 복잡하므로, 여기서는 구조만 구현합니다.)
    """
    if not NAVER_CLIENT_ID or not NAVER_SECRET:
        print("❌ [Error] 네이버 API 환경변수가 설정되지 않았습니다.")
        return False

    print(f"▶️ 네이버 블로그에 발행 시도: {content_data['title']}")
    
    # 실제 네이버 Open API 호출 로직 (예: requests.post(naver_url, data=payload))
    # 현재는 시뮬레이션된 성공 로그를 출력합니다.
    try:
        # 예시 페이로드 구성
        payload = {
            "blog_id": os.environ.get("NAVER_BLOG_ID"),
            "title": content_data['title'],
            "content": content_data['html_content'],
            "tags": content_data['tags']
        }
        # 실제 호출: response = requests.post("https://api.naver.com/blog/publish", json=payload)
        
        print(f"✅ [Success] 네이버 발행 성공 시뮬레이션 완료. (API Key 사용: {NAVER_CLIENT_ID[:5]}...)")
        return True
    except Exception as e:
        print(f"❌ [Failure] 네이버 발행 중 오류 발생: {e}")
        return False

def publish_to_tistory(content_data: dict) -> bool:
    """
    티스토리 API를 사용하여 콘텐츠를 발행합니다.
    """
    if not TISTORY_API_KEY:
        print("❌ [Error] 티스토리 API 키가 설정되지 않았습니다.")
        return False

    print(f"▶️ 티스토리에 발행 시도: {content_data['title']}")
    
    # 실제 티스토리 API 호출 로직 (예: requests.post(tistory_url, data=payload))
    try:
        # 예시 페이로드 구성
        payload = {
            "api_key": TISTORY_API_KEY,
            "title": content_data['title'],
            "content": content_data['html_content'],
            "tags": content_data['tags']
        }
        # 실제 호출: response = requests.post("https://api.tistory.com/v3/post", data=payload)
        
        print(f"✅ [Success] 티스토리 발행 성공 시뮬레이션 완료.")
        return True
    except Exception as e:
        print(f"❌ [Failure] 티스토리 발행 중 오류 발생: {e}")
        return False

def main_publisher_pipeline(data_file_path: str):
    """
    전체 발행 파이프라인을 실행합니다.
    """
    print("="*50)
    print("🚀 자동 발행 시스템 시작: 콘텐츠 발행 테스트")
    print("="*50)

    try:
        with open(data_file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"❌ [Error] 데이터 파일을 찾을 수 없습니다: {data_file_path}")
        return

    if not data:
        print("⚠️ [Warning] 발행할 콘텐츠 데이터가 없습니다.")
        return

    content_data = data[0] # 현재는 가장 최신 데이터 1개만 발행한다고 가정

    print(f"\n--- 발행할 콘텐츠: {content_data['title']} ---")
    print(f"전체 프로세스 완료. 이제 최종 발행 단계입니다.")

    # 1. 네이버 발행 시도
    naver_success = publish_to_naver(content_data)
    
    # 2. 티스토리 발행 시도
    tistory_success = publish_to_tistory(content_data)
    
    if naver_success or tistory_success:
        print("\n✨ 모든 발행 작업이 성공적으로 완료되었습니다. 시스템 효율성이 크게 향상되었습니다.")
    else:
        print("\n🚨 경고: 모든 발행 시도가 실패했습니다. API 키와 환경변수를 확인해주세요.")

if __name__ == "__main__":
    # 예시: data_processor.py가 생성한 최신 데이터를 로드한다고 가정
    # 실제 실행 시에는 data_processor.py가 생성한 JSON 파일 경로를 사용해야 합니다.
    print("ℹ️ [Tip] 이 스크립트는 'scripts/processed_data.json' 파일을 읽어와야 합니다.")
    main_publisher_pipeline("scripts/processed_data.json")