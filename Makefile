RPMBUILD = rpmbuild --define "_topdir %(pwd)/build" \
        --define "_builddir %{_topdir}" \
        --define "_rpmdir %{_topdir}" \
        --define "_srcrpmdir %{_topdir}" \
        --define "_sourcedir %(pwd)"

all:
	mkdir -p build
	${RPMBUILD} --define "_version $$(date --utc +%Y%m%d%H%M%S)" -ba rockit-camera.spec
	mv build/noarch/*.rpm .
	rm -rf build

install:
	@sudo cp cam /bin/
	@sudo cp completion/cam /etc/bash_completion.d/
	@echo ""
	@echo "Installed client files."
