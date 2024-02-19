from delivery_agent.models import DeliveryAgent
from accounts.models import UserType, User


def get_agent_list():
    agent_list = []
    for agent in DeliveryAgent.objects.filter(is_active=True):
        agent_list.append(agent)
    return {"agent_list": agent_list}


def get_agent_detail(agent_id):
    agent = DeliveryAgent.objects.get(id=agent_id)
    return {
        "id": agent_id,
        "username": agent.user.username,
        "name": agent.user.name,
        "mobile": agent.user.mobile,
    }


def update_agent(request, agent_id):
    agent = DeliveryAgent.objects.get(id=agent_id, is_active=True)
    agent_user = agent.user
    agent_user.username = request.POST.get("username")
    agent_user.name = request.POST.get("name")
    agent_user.mobile = request.POST.get("mobile")
    agent_user.save()


def create_agent(request):
    agent_user = User(
        username=request.POST.get("username"),
        name=request.POST.get("name"),
        mobile=request.POST.get("mobile"),
        type=UserType.TEACHER,
    )
    agent_user.set_password("1234")
    agent_user.full_clean()
    agent_user.save()
    DeliveryAgent.objects.create(
        user=agent_user, created_by=request.user, modified_by=request.user
    )


def delete_agent(request, agent_id):
    agent = DeliveryAgent.objects.get(id=agent_id)
    agent.is_active = False
    agent.modified_by = request.user
    agent.save()
    agent_user = agent.user
    agent_user.is_disabled = True
    agent_user.save()
