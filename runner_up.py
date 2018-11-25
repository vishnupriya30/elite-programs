def runner_up(scores):
     scores = list(set(scores))
     scores.sort()
     return (scores[-2])
def main():
     n = int(input("no of players:"))
     scores = []
     for  i in range(0, n):
          scores.append(input())
     print("Score of runner up is", runner_up(scores))
     return None
main()
