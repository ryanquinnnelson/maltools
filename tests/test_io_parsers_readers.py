import maltools

EXAMPLE = """<?xml version="1.0" encoding="UTF-8" ?>
    <!--
     Created by XML Export feature at MyAnimeList.net
     Version 1.1.0
    -->
    
    <myanimelist>
    
        <myinfo>
            <user_id>123456789</user_id>
            <user_name>username</user_name>
            <user_export_type>1</user_export_type>
            <user_total_anime>2</user_total_anime>
            <user_total_watching>0</user_total_watching>
            <user_total_completed>2</user_total_completed>
            <user_total_onhold>5</user_total_onhold>
            <user_total_dropped>3</user_total_dropped>
            <user_total_plantowatch>4</user_total_plantowatch>
        </myinfo>
    
    
            <anime>
                <series_animedb_id>41380</series_animedb_id>
                <series_title><![CDATA[100-man no Inochi no Ue ni Ore wa Tatteiru]]></series_title>
                <series_type>TV</series_type>
                <series_episodes>12</series_episodes>
                <my_id>0</my_id>
                <my_watched_episodes>2</my_watched_episodes>
                <my_start_date>0000-00-00</my_start_date>
                <my_finish_date>0000-00-00</my_finish_date>
                <my_rated></my_rated>
                <my_score>7</my_score>
                <my_storage></my_storage>
                <my_storage_value>0.00</my_storage_value>
                <my_status>Plan to Watch</my_status>
                <my_comments><![CDATA[]]></my_comments>
                <my_times_watched>0</my_times_watched>
                <my_rewatch_value></my_rewatch_value>
                <my_priority>LOW</my_priority>
                <my_tags><![CDATA[Crunchyroll, isekai, fantasy,MAYBE_BUY]]></my_tags>
                <my_rewatching>0</my_rewatching>
                <my_rewatching_ep>0</my_rewatching_ep>
                <my_discuss>1</my_discuss>
                <my_sns>default</my_sns>
                <update_on_import>0</update_on_import>
            </anime>
        
            <anime>
                <series_animedb_id>31646</series_animedb_id>
                <series_title><![CDATA[3-gatsu no Lion]]></series_title>
                <series_type>TV</series_type>
                <series_episodes>22</series_episodes>
                <my_id>0</my_id>
                <my_watched_episodes>1</my_watched_episodes>
                <my_start_date>0000-00-00</my_start_date>
                <my_finish_date>0000-00-00</my_finish_date>
                <my_rated></my_rated>
                <my_score>6</my_score>
                <my_storage></my_storage>
                <my_storage_value>0.00</my_storage_value>
                <my_status>Dropped</my_status>
                <my_comments><![CDATA[]]></my_comments>
                <my_times_watched>0</my_times_watched>
                <my_rewatch_value></my_rewatch_value>
                <my_priority>LOW</my_priority>
                <my_tags><![CDATA[Studio Shaft, mangaka Chica Umino, boring, slow]]></my_tags>
                <my_rewatching>0</my_rewatching>
                <my_rewatching_ep>0</my_rewatching_ep>
                <my_discuss>1</my_discuss>
                <my_sns>default</my_sns>
                <update_on_import>0</update_on_import>
            </anime>
        
            
        
        </myanimelist>
        
"""


def test_read_xml(tmpdir):
    p = tmpdir / "anime.xml"
    p.write_text(EXAMPLE, encoding=None)
    df = maltools.read_xml(p)
    assert df.shape == (2, 23)
