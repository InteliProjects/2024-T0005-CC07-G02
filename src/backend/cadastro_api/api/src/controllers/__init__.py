from flask import Blueprint, request, Response, json
## from src.services.user_service import UserService

class Usuario_Controller(Blueprint):
    def __init__(self, name, import_name):
        super().__init__(name, import_name)

        self.route('/usuarios', methods=['GET'])(self.get_all_users)
        self.route('/usuarios/<string(36):id>', methods=['GET'])(self.get_by_id)
        self.route('/usuarios', methods=['POST'])(self.create)
        self.route('/usuarios/<string(36):id>', methods=['PUT'])(self.update)
        self.route('/usuarios/<string(36):id>', methods=['DELETE'])(self.delete)
    
    def get_all_users(self):
        response_data, status_code = User_Service().get_all_users()

        return Response(
            response=json.dumps('get_all'),
            status=status_code,
            mimetype='application/json'
        )

    def get_by_id(self, id):
        return 'get_by_id'

    def create(self):
        return 'create'

    def update(self, id):
        return 'update'

    def delete(self, id):
        return 'delete'