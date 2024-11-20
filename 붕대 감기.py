#다 감으면 tx + y, 중간에 끊기면 tx
#bandage = [기술시전시간 t, 1초회복량 x, 추가회복량 y]
#health = 최대체력
#attacks = [공격시점, 피해량]

def solution(bandage, health, attacks):
    answer = 0
    current_health = health
    current_t = 0
    while attacks:
        this_attack = attacks.pop(0)
        this_attack_time, this_attack_dmg = this_attack[0], this_attack[1]
        current_health += (this_attack_time - current_t - 1) * bandage[1] + ((this_attack_time - current_t - 1) // bandage[0]) * bandage[2]
        if current_health > health:
            current_health = health
        current_health -= this_attack_dmg
        if current_health <= 0:
            return -1
        current_t = this_attack_time
    return current_health if current_health > 0 else -1