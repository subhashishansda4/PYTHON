# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 14:29:22 2022

@author: VAGUE
"""

# web scraping sudokukingdom.com
# entering puzzle into a list
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import sudoku

driver = webdriver.Chrome()
driver.get("https://sudokukingdom.com/")
#assert "Sudoku" in driver.title

driver.fullscreen_window()
# select expert difficulty
driver.find_element(By.ID, "g4").click()

r = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
c = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
puzzle = [[]]

#"vc_" + c[j] + "_" + r[i]

# Continously solve forever
# Remove loop to only solve once
while True:
    time.sleep(2)  # Wait for expert mode to load
    for i in range(9):
        r.append(i)
        for j in range(9):
            c.append(j)
            cell = driver.find_element(By.ID, "vc_" + c[j] + "_" + r[i])
            value = cell.getText()
            puzzle[i][j].append(value)
        
print(puzzle)

backup_puzzle = list(map(list, puzzle))
sudoku.solve_sudoku(puzzle)

    

# =============================================================================
#     backup_table = list(map(list, sudokuTable))
#     solve(sudokuTable)
# 
#     # I couldn't get selenium to type numbers as there is no clear textbox
#     # Thankfully there was a numpad :)
#     numpad = driver.find_elements_by_class_name("numpad-item")
#     # Replaces all 0's with their solved value
#     for yp, y in enumerate(backup_table):
#         for xp, x in enumerate(y):
#             if x == 0:
#                 allCells[yp*9 + xp].click()
#                 numpad[sudokuTable[yp][xp] - 1].click()
#         # Selenium might generate an error if it can't click on the cell
#         # This is especially true on lower resolution displays
#         # Lower this value if that's the case, to trigger a scroll earlier
#         if yp == 6:
#             driver.execute_script("arguments[0].scrollIntoView();", gameTable)
# 
#     play_again = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.CLASS_NAME, "button-play"))
#         )
#     # Waits 2 seconds and resets the game
#     # Remove if you only want to solve once
#     time.sleep(2)
#     driver.execute_script("arguments[0].click();", play_again)
# =============================================================================