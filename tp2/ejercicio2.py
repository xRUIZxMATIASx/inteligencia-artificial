import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib
import matplotlib.pyplot as plt

relative_dis = ctrl.Antecedent(np.arange(0, 10, 1), "relative_dis")
relative_dis["low"] = fuzz.trimf(relative_dis.universe, [0, 0, 2])
relative_dis["medium"] = fuzz.trimf(relative_dis.universe, [1, 3, 6])
relative_dis["high"] = fuzz.trapmf(relative_dis.universe, [5, 8, 9, 9])
relative_dis.view()

aw_time = ctrl.Antecedent(np.arange(0, 10, 1), "aw_time")
aw_time["low"] = fuzz.trapmf(relative_dis.universe, [0, 0, 2, 4])
aw_time["medium"] = fuzz.trimf(relative_dis.universe, [2, 4.5, 7])
aw_time["high"] = fuzz.trapmf(relative_dis.universe, [5, 7, 9, 9])
aw_time.view()

capacity = ctrl.Antecedent(np.arange(0, 10, 1), "capacity")
capacity["low"] = fuzz.trapmf(relative_dis.universe, [0, 0, 2, 4])
capacity["medium"] = fuzz.trimf(relative_dis.universe, [2, 4.5, 7])
capacity["high"] = fuzz.trapmf(relative_dis.universe, [5, 7, 9, 9])
capacity.view()

priority = ctrl.Consequent(np.arange(0, 1, 0.25), "priority")
priority["low"] = fuzz.trimf(relative_dis.universe, [0, 0, 0.5])
priority["medium"] = fuzz.trimf(relative_dis.universe, [0.25, 0.5, 0.75])
priority["high"] = fuzz.trimf(relative_dis.universe, [0.5, 1, 1])
priority.view()
#plt.show()


priority.defuzzify_method = "mom"

rules = []
rules.append(ctrl.Rule(relative_dis["low"] and aw_time["low"] and capacity["low"], priority["high"]))
rules.append(ctrl.Rule(capacity["high"] or aw_time["high"] or relative_dis["high"], priority["low"]))
rules.append(ctrl.Rule(capacity["medium"] and (aw_time["medium"] and relative_dis["medium"]), priority["medium"]))

crtSys = ctrl.ControlSystem(rules)
elevators = ctrl.ControlSystemSimulation(crtSys)
elevators.input["capacity"] = 4
elevators.input["relative_dis"] = 2
elevators.input["aw_time"] = 2
elevators.compute()
elevators.print_state()
#elevators.view(sim=elevators)
print(f"prioridad: {elevators.output['priority']}")
