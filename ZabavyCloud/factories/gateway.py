from ..models.gateway import GatewayModel


class GatewayFactory:
    def __call__(self, *args, **kwargs) -> GatewayModel:
        return GatewayModel(*args, **kwargs)
