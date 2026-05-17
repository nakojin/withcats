import re

def extract_keywords(text: str) -> list[str]:
    """본문에서 주요 키워드를 추출합니다 (간단한 구현)."""
    # 실제로는 NLP 모델을 사용해야 하지만, 현재는 간단한 패턴 매칭 사용
    keywords = re.findall(r'[가-힣]{2,4}', text)
    return list(set(keywords))[:3] # 최대 3개 키워드 반환

def apply_keyword_tips(original_content: str, keywords: list[str]) -> str:
    """
    추출된 키워드를 바탕으로 전문가적 조언(팁)을 본문에 자동 삽입합니다.
    이것이 '지능형' 자동화의 핵심입니다.
    """
    if not keywords:
        return original_content
    
    keyword_str = ", ".join(keywords)
    tip_section = (
        "\n\n💡 **[전문가 꿀팁]**\n"
        f"위 내용을 바탕으로, '{keyword_str}'에 대한 관점에서 접근하면 더욱 깊이 있는 정보를 제공할 수 있습니다. "
        "실제 사용 시 이 키워드들을 제목이나 소제목에 활용하는 것을 추천합니다.\n"
        "궁금한 점은 댓글로 남겨주세요!"
    )
    
    # 결론 직전에 팁 섹션을 삽입하는 로직 (간단하게 원본 끝에 추가)
    return original_content.strip() + tip_section

# 테스트용 코드
if __name__ == '__main__':
    test_text = "뷰티 루틴을 지키는 것이 중요합니다. 기초 제품을 꼼꼼히 바르는 것이 핵심입니다."
    kws = extract_keywords(test_text)
    print(f"추출된 키워드: {kws}")
    enhanced = apply_keyword_tips(test_text, kws)
    print("\n--- 강화된 콘텐츠 예시 ---\n", enhanced)