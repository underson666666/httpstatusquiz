# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from const import *
import csv

def main():
    html = get_target_site_html()
    soup = BeautifulSoup(html, "html.parser")

    selector = "#wikiArticle > dl:nth-child(7) > dt:nth-child(3) > a:nth-child(1) > code:nth-child(1)"  # [<code>101 Switching Protocol</code>]
    selector = "#wikiArticle > dl:nth-child(7) > dt:nth-child(1) > a:nth-child(1) > code:nth-child(1)"  # [<code>100 Continue</code>]
    selector = "#wikiArticle > dl:nth-child(9) > dt:nth-child(1) > a:nth-child(1) > code:nth-child(1)"  # [<code>200</code>]
    selector = "#wikiArticle > dl:nth-child(9) > dt:nth-child(3) > a:nth-child(1) > code:nth-child(1)"  # [<code>201</code>]

    _has_next_code = True
    _has_next_hunders = True
    _hunders = 7
    _init_counter = 1
    _counter = 1
    _hunders_step = 2
    _counter_step = 2
    status_code_list = list()
    base_selector = "#wikiArticle > dl:nth-child(__HUNDREDS__) > dt:nth-child(__COUNTER__) > a:nth-child(1) > code:nth-child(1)"
    while _has_next_hunders:
        selector = selector_replace(base_selector, _hunders, _counter)
        text = get_target_text(soup, selector)

        # 成功時
        if text is not None:
            _has_next_code = True
            _counter += _counter_step


        # 失敗時
        elif text is None:
            if _has_next_code is False:
                _has_next_hunders = False
            else:
                _has_next_code = False
                _hunders += _hunders_step
                _counter = _init_counter

        if text is not None:
            modified_text = text.split(" ", 1)
            modified_text.append("")    # 将来のためにdetail用カラムを用意
            status_code_list.append(modified_text)

    write_status_codes_2_csv(status_code_list)


def selector_replace(selector, hunders, counter):
    selector = selector.replace("__HUNDREDS__", str(hunders)).replace("__COUNTER__", str(counter))
    selector = selector.replace("__COUNTER__", str(counter))
    return selector

def get_target_site_html():
    res = requests.get(URL)
    return res.text

def get_target_text(soup, css_selector):
    _ = soup.select_one(css_selector)
    if _ is None:
        return None
    return _.get_text()

def write_status_codes_2_csv(data):
    data.insert(0, ["code", "message", "detail"])
    with open(OUTPUT_FILE_NAME, "w") as f:
        writer = csv.writer(f)
        writer.writerows(data)


if __name__ == "__main__":
    main()

