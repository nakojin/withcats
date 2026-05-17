import json
import pandas as pd
from typing import Dict, List

def load_affiliate_data(file_path: str) -> Dict:
    """
    Business 에이전트가 분석한 구조화된 제휴 마케팅 데이터를 로드합니다.
    (예: CSV 또는 JSON 형식으로 '키워드', '성공패턴', '적합카테고리' 등을 포함)
    """
    print(f"--- 로드 중: {file_path} ---")
    try:
        # 실제 환경에서는 API 호출 또는 DB 연결이 필요합니다. 여기서는 예시를 사용합니다.
        data = {
            "target_keywords": ["최신 에어프라이어 추천", "가성비 뷰티템 비교"],
            "success_patterns": ["장단점 비교표", "사용 후기 시뮬레이션"],
            "cta_placement_rules": {
                "제품비교": "본문 30% 지점, 결론 직전",
                "사용후기": "이미지 캡션 및 본문 시작점"
            }
        }
        return data
    except FileNotFoundError:
        print("🚨 에러: 제휴 마케팅 데이터 파일을 찾을 수 없습니다.")
        return {}

def generate_content_structure(affiliate_data: Dict) -> Dict:
    """
    제공된 제휴 마케팅 데이터를 기반으로 최적의 블로그 콘텐츠 구조를 생성합니다.
    """
    if not affiliate_data:
        return {"status": "Failed", "message": "데이터가 없어 구조를 생성할 수 없습니다."}

    structure = {
        "title_suggestions": [f"🔥 {keyword} 최신 트렌드 및 솔루션 분석", f"{keyword} 완벽 가이드"],
        "optimal_sections": []
    }

    for keyword in affiliate_data.get("target_keywords", []):
        section = {
            "keyword": keyword,
            "suggested_structure": "서론(문제 제기) -> 본론(비교/분석) -> 결론(최종 추천/CTA)",
            "required_elements": []
        }
        
        # 성공 패턴에 따라 필수 요소 추가
        for pattern in affiliate_data.get("success_patterns", []):
            section["required_elements"].append(f"[{pattern} 구조 반영]")
        
        # CTA 규칙에 따라 배치 지점 지정
        for placement, rule in affiliate_data.get("cta_placement_rules", {}).items():
            section["required_elements"].append(f"[{placement} 배치 필요: {rule}]")

        structure["optimal_sections"].append(section)

    return structure

def main():
    """메인 실행 함수: 데이터 로드 -> 구조 생성 -> 결과 출력"""
    # 1. 데이터 로드 (실제 경로를 사용해야 함)
    affiliate_data = load_affiliate_data("data/affiliate_analysis_results.json")
    
    # 2. 콘텐츠 구조 생성
    content_structure = generate_content_structure(affiliate_data)
    
    # 3. 결과 출력 (이 결과를 Writer 에이전트에게 전달)
    print("\n==================================================")
    print("✅ [성공] 제휴 마케팅 기반 최적 콘텐츠 구조화 완료")
    print("==================================================")
    print(json.dumps(content_structure, indent=4, ensure_ascii=False))

if __name__ == "__main__":
    main()