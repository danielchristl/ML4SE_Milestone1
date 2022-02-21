# This is a sample Python script.
from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput

import sys
import astpretty
import ast
import staticfg
from staticfg import CFGBuilder
import pycallgraph
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def load_SVM():
    print("IN load")
    # iris = datasets.load_iris()
    # clf = svm.SVC(gamma=0.001, C=100.)
    # params = {"clf": clf, "iris": iris}
    return

# @workflow.step(catch_exceptions=True)
def fit_SVM():
    print("IN fit")
    # clf = something[0]["clf"]
    # iris = something[0]["iris"]
    # clf.fit(iris.data[:-1], iris.target[:-1])
    # params = {"clf": clf, "iris": iris}
    return

# @workflow.step(catch_exceptions=True)
def pred_SVM():
    print("IN pred")
    # clf = something[0]["clf"]
    # iris = something[0]["iris"]
    # preds = clf.predict(iris.data[-1:])
    return



def runRay():
    # ray.shutdown()
    # workflow.init(storage="/tmp/data") ## storage="/tmp/data"

    # current_time = datetime.now().time() # get time for unique Workflow ID
    # workflowID = f"rayWorkflow-scikitlearn-{current_time}"

    # load_SVM.step().run(workflowID)
    # clfIrisDict.run(workflowID)
    # clfIrisDict = fit_SVM.step( clfIrisDict)
    # preds = pred_SVM.step( clfIrisDict)

    # run workflow
    # preds.run(workflowID)

    # get result
    # preds = ray.get(workflow.get_output(workflowID))
    # print(preds)
    # preds = make_np_serializable(preds[0][0])
    print("hi")
    load_SVM()
    fit_SVM()
    pred_SVM()
    return -1




def main(argv):
    if argv[0] == "--help":
        print("Use --representation to see a certain representation. Valid arguments are AST CG CFG")
        print("Example: python3 milestone1.py --representation AST --input [path to a file name]")
        print("Example: python3 milestone1.py --representation AST")
        print("Use --help to see this message.")

    elif len(argv) != 2:
        print("INVALID ARGUMENT. Use --help to see commands")

    elif argv[0] == "--representation" and argv[1].upper() in ["AST", "CG", "CFG"]:
        if argv[1].upper() == "AST":
            # AST code here
            print("AST outputting...")
            target = """
def step(*args, **kwargs):
    if len(args) == 1 and len(kwargs) == 0 and callable(args[0]):
        options = WorkflowStepRuntimeOptions.make(step_type=StepType.FUNCTION)
        return make_step_decorator(options)(args[0])
    if len(args) != 0:
        raise ValueError(f"Invalid arguments for step decorator {args}")
    max_retries = kwargs.pop("max_retries", None)
    catch_exceptions = kwargs.pop("catch_exceptions", None)
    name = kwargs.pop("name", None)
    metadata = kwargs.pop("metadata", None)
    allow_inplace = kwargs.pop("allow_inplace", False)
    ray_options = kwargs

    options = WorkflowStepRuntimeOptions.make(
        step_type=StepType.FUNCTION,
        catch_exceptions=catch_exceptions,
        max_retries=max_retries,
        allow_inplace=allow_inplace,
        ray_options=ray_options,
    )
return make_step_decorator(options, name, metadata)
            """

            astpretty.pprint(ast.parse(target))


        elif argv[1].upper() == "CG":
            # CG code here
            print("CG outputting...")

            with PyCallGraph(output=GraphvizOutput()):
                runRay()
            print("CG outputted as pycallgraph.png")

        elif argv[1].upper() == "CFG":
            # CFG code here
            print("CFG outputting...")
            cfg = CFGBuilder().build_from_file('api.py',
                                               'api.py')

            cfg.build_visual('RayWorkflows_api_CFG', 'pdf')
            print("CFG outputted as RayWorkflows_api_CFG.png")



    else:
        print("INVALID ARGUMENT. Use --help to see commands")



if __name__ == '__main__':
    main(sys.argv[1:])




