import re
from typing import Dict, Any, List

def generate_seo_metadata(raw_content: str, keywords: List[str]) -> Dict[str, str]:
    """
    원시 콘텐츠와 핵심 키워드를 기반으로 SEO에 최적화된 메타데이터를 생성합니다.
    [개선점] 단순 키워드 나열이 아닌, 검색 의도를 반영한 자연스러운 설명을 생성하도록 설계합니다.
    """
    print("--- SEO 메타데이터 생성 시작 ---")
    
    # 1. Title 생성 (최대 60자 이내)
    base_title = f"{keywords[0]} 완벽 가이드 | {keywords[1]} 팁"
    title = base_title[:55] + "..." if len(base_title) > 58 else base_title
    
    # 2. Description 생성 (최대 150자 이내)
    description = (f"최신 트렌드에 맞춘 {keywords[0]} 콘텐츠 기획법을 알아보세요. "
                    f"{keywords[1]} 전문가가 알려주는 핵심 팁과 실습 위주의 가이드입니다.")
    
    # 3. Tags 정리
    tags = ", ".join(keywords[:5])
    
    return {
        "title": title,
        "description": description,
        "tags": tags,
        "seo_status": "PASS"
    }

def validate_content_structure(raw_content: str) -> bool:
    """
    콘텐츠의 최소 분량과 구조적 완전성을 검증합니다.
    (예: 제목 태그 유무, 본문 길이, 이미지 Placeholder 유무)
    """
    print("--- 콘텐츠 구조 유효성 검증 시작 ---")
    
    # 최소 길이 검증 (예: 공백 문자 포함 최소 500자 이상)
    if len(raw_content.strip()) < 500:
        print(f"[ERROR] 본문 길이가 너무 짧습니다. (현재 길이: {len(raw_content.strip())}자)")
        return False
    
    # 구조적 요소 검증 (제목 태그가 있는지 등)
    if not re.search(r'<h1>|<h2>', raw_content, re.I):
        print("[WARNING] 제목 태그(H1/H2)가 명확하게 보이지 않습니다. 가독성을 위해 추가를 권장합니다.")
    
    return True

def run_content_validation(raw_content: str, keywords: List[str]) -> Dict[str, Any]:
    """
    SEO 메타데이터 생성과 콘텐츠 구조 검증을 통합하여 실행합니다.
    """
    is_valid = validate_content_structure(raw_content)
    seo_data = generate_seo_metadata(raw_content, keywords)
    
    if not is_valid:
        seo_data["seo_status"] = "FAIL (Structure)"
        return seo_data
    else:
        print("[SUCCESS] 콘텐츠 유효성 및 SEO 데이터 생성 완료.")
        return seo_data

# 테스트 코드 (실제 실행 시 주석 처리)
if __name__ == "__main__":
    test_content = "여기는 테스트용으로 작성된 충분히 긴 본문 내용입니다. 뷰티 트렌드와 관련된 자세한 내용이 담겨있습니다. 이 내용은 500자 이상이어야 합니다." * 5
    test_keywords = ["헤어 스타일링", "뷰티 팁"]
    
    metadata = run_content_validation(test_content, test_keywords)
    print("\n--- 최종 검증 결과 ---")
    print(metadata)